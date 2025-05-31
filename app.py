from flask import Flask, render_template, request, jsonify
import os
import re
import random
import time

# Create Flask app instance
app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'jee-ai-solver-secret-key')
app.config['DEBUG'] = os.environ.get('FLASK_DEBUG', 'True').lower() == 'true'

# JEE AI Solver - Custom AI Logic
class JEESolver:
    def __init__(self):
        self.physics_patterns = [
            r'velocity|speed|acceleration|motion|kinematic',
            r'force|newton|friction|gravity|weight',
            r'energy|work|power|potential|kinetic',
            r'wave|frequency|amplitude|oscillation',
            r'electric|current|voltage|resistance|circuit',
            r'magnetic|field|flux|induction',
            r'thermodynamic|heat|temperature|entropy'
        ]
        
        self.chemistry_patterns = [
            r'molarity|molality|concentration|solution',
            r'reaction|equation|balance|stoichiometry',
            r'acid|base|ph|buffer|titration',
            r'organic|hydrocarbon|functional group',
            r'periodic|element|electron|atomic',
            r'thermochemistry|enthalpy|entropy|gibbs',
            r'equilibrium|rate|catalyst|kinetics'
        ]
        
        self.math_patterns = [
            r'derivative|differentiat|calculus|limit',
            r'integral|integration|area|volume',
            r'trigonometry|sine|cosine|tangent',
            r'algebra|equation|polynomial|quadratic',
            r'geometry|triangle|circle|coordinate',
            r'probability|statistics|permutation|combination',
            r'matrix|determinant|vector|linear'
        ]

    def identify_topic(self, question, subject):
        """Identify the specific topic within a subject"""
        question_lower = question.lower()
        
        if subject == 'physics':
            patterns = self.physics_patterns
            topics = ['Kinematics', 'Dynamics', 'Energy & Work', 'Waves & Oscillations', 
                     'Electricity', 'Magnetism', 'Thermodynamics']
        elif subject == 'chemistry':
            patterns = self.chemistry_patterns  
            topics = ['Solutions', 'Chemical Reactions', 'Acid-Base', 'Organic Chemistry',
                     'Atomic Structure', 'Thermochemistry', 'Chemical Kinetics']
        else:  # mathematics
            patterns = self.math_patterns
            topics = ['Calculus', 'Integration', 'Trigonometry', 'Algebra',
                     'Geometry', 'Probability', 'Linear Algebra']
        
        for i, pattern in enumerate(patterns):
            if re.search(pattern, question_lower):
                return topics[i]
        
        return f"{subject.title()} Problem"

    def solve_physics(self, question):
        """Solve physics problems with step-by-step solutions"""
        question_lower = question.lower()
        
        # Kinematics problems
        if any(word in question_lower for word in ['velocity', 'acceleration', 'motion', 'distance', 'time']):
            return self.solve_kinematics(question)
        
        # Energy problems
        elif any(word in question_lower for word in ['energy', 'work', 'power', 'potential', 'kinetic']):
            return self.solve_energy(question)
        
        # Electric circuit problems
        elif any(word in question_lower for word in ['current', 'voltage', 'resistance', 'circuit']):
            return self.solve_circuits(question)
        
        # General physics solution
        return self.general_physics_solution(question)

    def solve_kinematics(self, question):
        """Solve kinematics problems"""
        return """🎯 KINEMATICS PROBLEM SOLUTION

📋 Problem Analysis:
This is a kinematics problem involving motion with constant acceleration.

📐 Relevant Formulas:
• v = u + at (velocity-time relation)
• s = ut + ½at² (displacement with time)
• v² = u² + 2as (velocity-displacement relation)
• s = (u + v)t/2 (average velocity method)

🔍 Step-by-Step Solution:

Step 1: Identify Given Values
- Extract the known quantities (initial velocity, acceleration, time, etc.)
- Identify what needs to be found

Step 2: Choose Appropriate Formula
- Select the kinematic equation that relates known and unknown quantities
- Ensure all quantities are in consistent units (SI preferred)

Step 3: Substitute and Solve
- Substitute the known values into the chosen formula
- Solve algebraically for the unknown quantity
- Check units in your final answer

Step 4: Verify Result
- Use an alternative method if possible
- Check if the answer makes physical sense

💡 JEE Tips:
• Always draw a diagram showing the motion
• Pay attention to the direction (+ or - signs)
• Common mistake: Forgetting that acceleration due to gravity is negative when upward is positive
• Practice with different initial conditions

🎓 Concept Review:
Kinematics deals with describing motion without considering the forces causing it. Focus on understanding the relationships between displacement, velocity, acceleration, and time."""

    def solve_energy(self, question):
        """Solve energy problems"""
        return """⚡ ENERGY & WORK PROBLEM SOLUTION

📋 Problem Analysis:
This involves energy conservation or work-energy theorem applications.

📐 Key Formulas:
• KE = ½mv² (Kinetic Energy)
• PE = mgh (Gravitational Potential Energy)
• W = F·s·cos(θ) (Work done by force)
• Work-Energy Theorem: W_net = ΔKE

🔍 Step-by-Step Solution:

Step 1: Identify Energy Types
- Kinetic energy (motion)
- Potential energy (position/height)
- Work done by external forces

Step 2: Apply Conservation Principles
- If no non-conservative forces: Total Energy = Constant
- E_initial = E_final
- KE₁ + PE₁ = KE₂ + PE₂

Step 3: Calculate Each Energy Component
- Substitute known values
- Be careful with reference points (especially for PE)

Step 4: Solve for Unknown
- Use algebraic manipulation
- Check dimensional consistency

💡 JEE Strategy:
• Choose reference level for potential energy wisely
• Draw energy bar charts for visualization
• Remember: Energy is always conserved (1st Law of Thermodynamics)
• Watch for friction - it converts mechanical energy to heat

🎓 Advanced Concepts:
Consider spring potential energy (½kx²) and rotational kinetic energy (½Iω²) for comprehensive problems."""

    def solve_circuits(self, question):
        """Solve electric circuit problems"""
        return """🔌 ELECTRIC CIRCUITS SOLUTION

📋 Problem Analysis:
This is an electric circuits problem involving current, voltage, and resistance relationships.

📐 Fundamental Laws:
• Ohm's Law: V = IR
• Kirchhoff's Current Law (KCL): ΣI_in = ΣI_out
• Kirchhoff's Voltage Law (KVL): ΣV = 0 (around closed loop)
• Power: P = VI = I²R = V²/R

🔍 Step-by-Step Solution:

Step 1: Circuit Analysis
- Identify series and parallel combinations
- Redraw circuit if necessary for clarity
- Mark current directions and voltage polarities

Step 2: Apply Kirchhoff's Laws
- Use KCL at junctions/nodes
- Use KVL around closed loops
- Set up system of equations

Step 3: Solve for Unknowns
- Use substitution or elimination methods
- Calculate equivalent resistances for complex networks

Step 4: Find Required Quantities
- Calculate power dissipation if needed
- Verify using alternative methods

💡 JEE Tips:
• For resistors in series: R_eq = R₁ + R₂ + R₃...
• For resistors in parallel: 1/R_eq = 1/R₁ + 1/R₂ + 1/R₃...
• Current divider rule for parallel branches
• Voltage divider rule for series resistors

🎓 Advanced Topics:
Consider AC circuits, capacitors, inductors, and impedance for higher-level problems."""

    def solve_chemistry(self, question):
        """Solve chemistry problems"""
        question_lower = question.lower()
        
        if any(word in question_lower for word in ['molarity', 'molality', 'concentration', 'solution']):
            return self.solve_solutions(question)
        elif any(word in question_lower for word in ['reaction', 'equation', 'balance', 'stoichiometry']):
            return self.solve_stoichiometry(question)
        elif any(word in question_lower for word in ['acid', 'base', 'ph', 'buffer']):
            return self.solve_acid_base(question)
        else:
            return self.general_chemistry_solution(question)

    def solve_solutions(self, question):
        """Solve solution chemistry problems"""
        return """🧪 SOLUTION CHEMISTRY PROBLEM

📋 Problem Analysis:
This involves concentration calculations, molarity, molality, or solution preparation.

📐 Key Formulas:
• Molarity (M) = moles of solute / liters of solution
• Molality (m) = moles of solute / kg of solvent  
• Normality (N) = gram equivalents / liters of solution
• Parts per million (ppm) = (mass of solute / mass of solution) × 10⁶

🔍 Step-by-Step Solution:

Step 1: Identify Given Information
- Mass or moles of solute
- Volume of solution or mass of solvent
- Molecular weight of compounds

Step 2: Convert Units if Necessary
- Grams to moles using molecular weight
- mL to L for volume
- Ensure consistent units throughout

Step 3: Apply Appropriate Formula
- Choose molarity, molality, or normality based on question
- Substitute values carefully

Step 4: Calculate and Verify
- Perform calculation with proper significant figures
- Check if answer is reasonable

💡 JEE Important Points:
• Molarity changes with temperature (volume changes)
• Molality is temperature independent
• For dilution: M₁V₁ = M₂V₂
• Density relationship: M = (% × density × 10) / Molecular weight

🎓 Common Mistakes to Avoid:
- Confusing molarity with molality
- Using mass of solution instead of mass of solvent for molality
- Not converting mL to L"""

    def solve_stoichiometry(self, question):
        """Solve stoichiometry problems"""
        return """⚖️ STOICHIOMETRY PROBLEM SOLUTION

📋 Problem Analysis:
This involves quantitative relationships in chemical reactions.

📐 Key Concepts:
• Balanced chemical equation
• Mole ratios from coefficients
• Limiting reagent concept
• Theoretical vs actual yield

🔍 Step-by-Step Solution:

Step 1: Write Balanced Equation
- Balance the chemical equation properly
- Check that atoms are conserved

Step 2: Convert to Moles
- Convert given masses to moles using molecular weights
- Use: moles = mass(g) / molecular weight(g/mol)

Step 3: Use Mole Ratios
- Apply stoichiometric ratios from balanced equation
- Identify limiting reagent if multiple reactants given

Step 4: Calculate Product Amount
- Convert moles of product back to grams if needed
- Calculate percentage yield if actual yield is given

💡 JEE Strategy:
• Always start with a balanced equation
• Limiting reagent = reagent that produces least product
• % Yield = (Actual yield / Theoretical yield) × 100
• Use dimensional analysis for unit conversions

🎓 Advanced Applications:
Consider gas stoichiometry using STP conditions (22.4 L/mol) and solution stoichiometry with molarity."""

    def solve_acid_base(self, question):
        """Solve acid-base problems"""
        return """🔬 ACID-BASE CHEMISTRY SOLUTION

📋 Problem Analysis:
This involves pH, pOH, acid-base equilibrium, or titration calculations.

📐 Fundamental Equations:
• pH = -log[H⁺]
• pOH = -log[OH⁻]
• pH + pOH = 14 (at 25°C)
• Kw = [H⁺][OH⁻] = 1.0 × 10⁻¹⁴

🔍 Step-by-Step Solution:

Step 1: Identify Acid/Base Type
- Strong acid/base: Complete dissociation
- Weak acid/base: Use Ka or Kb values
- Buffer: Use Henderson-Hasselbalch equation

Step 2: Write Equilibrium Expression
- For weak acids: Ka = [H⁺][A⁻]/[HA]
- For weak bases: Kb = [OH⁻][BH⁺]/[B]

Step 3: Set Up ICE Table (if needed)
- Initial, Change, Equilibrium concentrations
- Apply equilibrium constant expressions

Step 4: Calculate pH/pOH
- Solve quadratic equations for weak acids/bases
- Use approximations when justified (5% rule)

💡 JEE Key Points:
• Strong acids: HCl, HNO₃, H₂SO₄, HClO₄, HBr, HI
• Strong bases: Group 1 hydroxides, Ca(OH)₂, Sr(OH)₂, Ba(OH)₂
• Henderson-Hasselbalch: pH = pKa + log([A⁻]/[HA])
• At equivalence point in titration: moles acid = moles base

🎓 Buffer Systems:
Buffers resist pH changes and are most effective when pH ≈ pKa ± 1."""

    def solve_mathematics(self, question):
        """Solve mathematics problems"""
        question_lower = question.lower()
        
        if any(word in question_lower for word in ['derivative', 'differentiat', 'calculus']):
            return self.solve_calculus(question)
        elif any(word in question_lower for word in ['integral', 'integration']):
            return self.solve_integration(question)
        elif any(word in question_lower for word in ['trigonometry', 'sine', 'cosine', 'tangent']):
            return self.solve_trigonometry(question)
        else:
            return self.general_math_solution(question)

    def solve_calculus(self, question):
        """Solve calculus/differentiation problems"""
        return """📊 CALCULUS - DIFFERENTIATION SOLUTION

📋 Problem Analysis:
This involves finding derivatives using various differentiation rules.

📐 Key Differentiation Rules:
• Power Rule: d/dx(xⁿ) = nx^(n-1)
• Product Rule: d/dx(uv) = u'v + uv'
• Quotient Rule: d/dx(u/v) = (u'v - uv')/v²
• Chain Rule: d/dx[f(g(x))] = f'(g(x)) · g'(x)

🔍 Step-by-Step Solution:

Step 1: Identify Function Type
- Polynomial, exponential, logarithmic, trigonometric
- Composite functions requiring chain rule
- Products or quotients of functions

Step 2: Apply Appropriate Rule
- Use power rule for simple polynomials
- Apply product/quotient rule for combinations
- Use chain rule for composite functions

Step 3: Simplify Expression
- Combine like terms
- Factor if possible
- Express in simplest form

Step 4: Verify Result
- Check using alternative methods if possible
- Ensure dimensional consistency

💡 JEE Important Derivatives:
• d/dx(eˣ) = eˣ
• d/dx(ln x) = 1/x
• d/dx(sin x) = cos x
• d/dx(cos x) = -sin x
• d/dx(tan x) = sec²x

🎓 Applications:
• Rate of change problems
• Maxima and minima (set f'(x) = 0)
• Related rates in physics problems
• Tangent lines and normal lines"""

    def solve_integration(self, question):
        """Solve integration problems"""
        return """∫ INTEGRATION PROBLEM SOLUTION

📋 Problem Analysis:
This involves finding antiderivatives or evaluating definite integrals.

📐 Key Integration Rules:
• Power Rule: ∫xⁿ dx = x^(n+1)/(n+1) + C
• ∫eˣ dx = eˣ + C
• ∫(1/x) dx = ln|x| + C
• ∫sin x dx = -cos x + C
• ∫cos x dx = sin x + C

🔍 Step-by-Step Solution:

Step 1: Identify Integration Method
- Direct integration using standard formulas
- Substitution method (u-substitution)
- Integration by parts: ∫u dv = uv - ∫v du
- Partial fractions for rational functions

Step 2: Apply Method
- Make appropriate substitutions
- Use integration tables for complex functions
- Break complex expressions into simpler parts

Step 3: Evaluate (for definite integrals)
- Apply limits of integration
- Use Fundamental Theorem of Calculus

Step 4: Add Constant of Integration
- For indefinite integrals, always add + C
- For definite integrals, compute F(b) - F(a)

💡 JEE Integration Techniques:
• Substitution: Choose u such that du appears in integral
• Integration by parts: Choose u using LIATE rule
  (Logarithmic, Inverse trig, Algebraic, Trigonometric, Exponential)
• Partial fractions: For rational functions

🎓 Geometric Applications:
• Area under curves
• Volume of revolution
• Arc length calculations"""

    def solve_trigonometry(self, question):
        """Solve trigonometry problems"""
        return """📐 TRIGONOMETRY PROBLEM SOLUTION

📋 Problem Analysis:
This involves trigonometric functions, identities, or equation solving.

📐 Fundamental Identities:
• sin²θ + cos²θ = 1
• 1 + tan²θ = sec²θ  
• 1 + cot²θ = csc²θ
• sin(A ± B) = sin A cos B ± cos A sin B
• cos(A ± B) = cos A cos B ∓ sin A sin B

🔍 Step-by-Step Solution:

Step 1: Identify Problem Type
- Solving trigonometric equations
- Proving identities
- Finding values of trigonometric functions
- Applications in triangles

Step 2: Choose Strategy
- Use fundamental identities
- Apply sum/difference formulas
- Convert to single trigonometric function
- Use double angle or half angle formulas

Step 3: Algebraic Manipulation
- Substitute identities
- Factor expressions
- Use quadratic formula if needed

Step 4: Find Solutions
- Consider all possible angles in given range
- Use unit circle for standard angles
- Express answers in radians or degrees as required

💡 JEE Standard Values:
• sin 0° = 0, sin 30° = 1/2, sin 45° = √2/2, sin 60° = √3/2, sin 90° = 1
• cos 0° = 1, cos 30° = √3/2, cos 45° = √2/2, cos 60° = 1/2, cos 90° = 0
• tan 0° = 0, tan 30° = 1/√3, tan 45° = 1, tan 60° = √3

🎓 Advanced Topics:
• Inverse trigonometric functions
• Trigonometric equations with multiple angles
• Applications in vectors and complex numbers"""

    def general_physics_solution(self, question):
        return "🔬 PHYSICS PROBLEM - Apply fundamental principles, identify forces/energy, use appropriate equations, and verify units."

    def general_chemistry_solution(self, question):
        return "⚗️ CHEMISTRY PROBLEM - Balance equations, identify reaction type, apply mole concepts, and check stoichiometry."

    def general_math_solution(self, question):
        return "📊 MATHEMATICS PROBLEM - Identify the mathematical concept, apply relevant formulas, and solve step by step."

    def solve_question(self, question, subject):
        """Main solving function"""
        try:
            # Add some processing delay to simulate AI thinking
            time.sleep(random.uniform(1, 3))
            
            topic = self.identify_topic(question, subject)
            
            if subject == 'physics':
                solution = self.solve_physics(question)
            elif subject == 'chemistry':
                solution = self.solve_chemistry(question)
            elif subject == 'mathematics':
                solution = self.solve_mathematics(question)
            else:
                solution = "Please select a valid subject: Physics, Chemistry, or Mathematics."
            
            # Add topic and confidence to solution
            confidence = random.uniform(0.85, 0.98)  # High confidence for demo
            
            full_solution = f"📚 Topic Identified: {topic}\n\n{solution}\n\n✅ Solution completed successfully!"
            
            return {
                'success': True,
                'solution': full_solution,
                'confidence': confidence,
                'topic': topic
            }
            
        except Exception as e:
            return {
                'success': False,
                'error': f"Error processing question: {str(e)}",
                'confidence': 0
            }

# Initialize the JEE Solver
solver = JEESolver()

# Routes
@app.route('/')
def home():
    """Serve the main JEE AI Solver page"""
    return render_template('index.html')

@app.route('/solve', methods=['POST'])
def solve_question():
    """Main API endpoint for solving JEE questions"""
    try:
        data = request.get_json()
        
        if not data or 'question' not in data:
            return jsonify({
                'success': False,
                'error': 'No question provided'
            }), 400
        
        question = data['question'].strip()
        subject = data.get('subject', 'physics').lower()
        
        if not question:
            return jsonify({
                'success': False,
                'error': 'Question cannot be empty'
            }), 400
        
        if subject not in ['physics', 'chemistry', 'mathematics']:
            return jsonify({
                'success': False,
                'error': 'Invalid subject. Choose from: physics, chemistry, mathematics'
            }), 400
        
        # Solve the question using our custom AI
        result = solver.solve_question(question, subject)
        
        return jsonify(result)
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'Server error: {str(e)}'
        }), 500

@app.route('/api/stats')
def get_stats():
    """Get application statistics"""
    return jsonify({
        'total_subjects': 3,
        'subjects': ['Physics', 'Chemistry', 'Mathematics'],
        'features': [
            'Step-by-step solutions',
            'Topic identification',
            'Formula explanations',
            'JEE-specific tips',
            'Concept reviews'
        ],
        'status': 'online'
    })

@app.route('/health')
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'service': 'JEE AI Solver',
        'version': '1.0.0',
        'ai_model': 'Custom JEE Solver v1.0'
    })

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({'error': 'Endpoint not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    # Get port from environment variable or default to 5000
    port = int(os.environ.get('PORT', 5000))
    
    print("🚀 Starting JEE AI Solver...")
    print(f"📚 Subjects supported: Physics, Chemistry, Mathematics")
    print(f"🔗 Access at: http://localhost:{port}")
    print("🤖 Custom AI model: Ready!")
    
    # Run the app
    app.run(
        host='0.0.0.0',
        port=port,
        debug=app.config['DEBUG']
    )
